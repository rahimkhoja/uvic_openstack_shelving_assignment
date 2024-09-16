from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort, current_app, Response
from flask_sitemap import Sitemap
from models import sheldb, User, Subscription, MobileNumber, History, UserPreference, AssistantPreference 
from utils.utility import *
from datetime import datetime

def configure_routes(app):

    sitemap = Sitemap(app=app)

    @app.context_processor
    def inject_analytics():
        return dict(
            google_analytics_id=app.config['GOOGLE_ANALYTICS_ID'],
            google_site_verification=app.config['GOOGLE_SITE_VERIFICATION'],
            bing_site_verification=app.config['BING_SITE_VERIFICATION']
        )

    @app.after_request
    def add_header(response):
        # Ensure the endpoint is not None before checking its value
        if request.endpoint and 'static' not in request.endpoint:
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
        return response
    
    @app.route('/robots.txt')
    def robots_txt():
        base_url = request.url_root[:-1]  # Remove the trailing slash
        lines = [
            "User-Agent: *",
            "Allow: /",
            f"Sitemap: {base_url}/sitemap.xml"
        ]
        return Response("\n".join(lines), mimetype="text/plain")


    @app.route('/', methods=['GET', 'POST'])
    def defer_page():
        if session.get('user_provider_id'):
            member = check_user_subscription(session.get('user_provider_id'))
        else:
            member = check_user_subscription(None)
        current_app.logger.info('Info: Terms Page - Member Object: ' + str(member))
        menu = generate_menu(member)
        return render_template('terms.html', seometa=MetaTags, menu=menu)

    @app.route('/email/notification-deferral', methods=['POST'])
    def notification_deferral():
        data = request.json
        email_content = "Your shelving has been deferred to {date}".format(date=data['deferral_date'])
        if send_email_and_post_comment(data['email'], data['vmname'], data['deferral_date'], data['ticket_number'], email_content):
            return jsonify({'message': 'Deferral notification sent successfully'}), 200

    @app.route('/email/notification-no-deferral', methods=['POST'])
    def notification_no_deferral():
        data = request.json
        email_content = "No deferral was initiated for {vmname}".format(vmname=data['vmname'])
        if send_email_and_post_comment(data['email'], data['vmname'], data['deferral_date'], data['ticket_number'], email_content):
            return jsonify({'message': 'No-deferral notification sent successfully'}), 200

    @app.route('/email/cancel-shelving', methods=['POST'])
    def cancel_shelving():
        data = request.json
        email_content = "Shelving for {vmname} has been canceled".format(vmname=data['vmname'])
        if send_email_and_post_comment(data['email'], data['vmname'], data['deferral_date'], data['ticket_number'], email_content):
            # Close the ticket (dummy implementation)
            print(f"Ticket {data['ticket_number']} closed.")
            return jsonify({'message': 'Shelving cancellation notification sent successfully'}), 200

    @app.route('/email/complete-shelving', methods=['POST'])
    def complete_shelving():
        data = request.json
        email_content = "Shelving for {vmname} is now complete".format(vmname=data['vmname'])
        if send_email_and_post_comment(data['email'], data['vmname'], data['deferral_date'], data['ticket_number'], email_content):
            # Close the ticket (dummy implementation)
            print(f"Ticket {data['ticket_number']} closed.")
            return jsonify({'message': 'Shelving complete notification sent successfully'}), 200

    @app.route('/email/shelving-initiated', methods=['POST'])
    def shelving_initiated():
        data = request.json
        email_content = "Shelving for {vmname} has been initiated".format(vmname=data['vmname'])
        if send_email_and_post_comment(data['email'], data['vmname'], data['deferral_date'], data['ticket_number'], email_content):
            # Provide a new ticket number (dummy implementation)
            new_ticket_number = "12345"
            return jsonify({'message': 'Shelving initiated', 'ticket_number': new_ticket_number}), 200
    
    @sitemap.register_generator
    def index():
        yield 'index_page', {}
