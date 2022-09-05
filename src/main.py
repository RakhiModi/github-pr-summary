import requests
import json
from smtplib import SMTP
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pretty_html_table import build_table
import pandas as pd

REPO_URL = 'https://api.github.com/repos/helix-editor/helix/pulls?state=all&per_page=100'


def get_pr_data():
    response = requests.get(REPO_URL)
    data = response.json()
    json_str = json.dumps(data)
    response = json.loads(json_str)
    pr = []
    week_ago = datetime.now()-timedelta(days=7)
    print(week_ago)
    for i in response:
        updated_date = datetime.strptime(i['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
        if updated_date > week_ago:
            output = {
                "url": i['url'],
                "number": i['number'],
                "title": i['title'],
                "state": i['state'],
                "user": i['user']['login'],
                "created_at": i['created_at'],
                "updated_at": i['updated_at'],
                "closed_at": i['closed_at'],
                "merged_at": i['merged_at'],
                "assignees": i['assignees'],
                "requested_reviewers": i['requested_reviewers'],
                "review_comments_url": i['review_comments_url']
            }
            pr.append(output)
    return pr


def create_dataframe():
    pr_data = get_pr_data()
    with open("pr_data", "w") as f:
        json.dump(pr_data, f)
    with open("pr_data") as f:
        d = json.load(f)
        df = pd.DataFrame(columns=d[0].keys())
        for i in range(len(d)):
            df.loc[i] = d[i].values()
    return df


def create_html_table():
    dataframe = create_dataframe()
    output = build_table(dataframe, 'blue_light')
    send_mail(output)
    return "Mail sent successfully"


def print_mail():
    dataframe = create_dataframe()
    body = dataframe.to_string()
    msg = MIMEMultipart()
    msg['To'] = 'work.rakhimodi@gmail.com'
    msg['From'] = 'rmodi7502@gmail.com'
    msg['Subject'] = 'PR summary' # % time_stamp.strftime('%Y-%m-%d %H:%M:%S')

    print(msg.as_string())
    print(body)


def send_mail(body):
    msg = MIMEMultipart()
    msg['Subject'] = 'PR summary'  # % time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    msg['From'] = 'rmodi7502@gmail.com'
    msg['To'] = 'work.rakhimodi@gmail.com'

    body_content = body
    msg.attach(MIMEText(body_content, "html"))
    msg_body = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'XXXXXXXXXX')
    print(server.sendmail(msg['From'], msg['To'], msg['Subject'], msg_body))
    server.quit()


if __name__ == "__main__":
    print_mail()
    # create_html_table() ### For send_mail function to work
