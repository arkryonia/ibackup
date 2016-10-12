def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox482cde53f3634f3799f046fb0691c818.mailgun.org/messages",
        auth=("api", "key-6be34abfb50e0b0ca43816a6210eceb8"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox482cde53f3634f3799f046fb0691c818.mailgun.org>",
              "to": "IRGIB <hello@irgib-africa.org>",
              "subject": "Hello IRGIB",
              "text": "Congratulations IRGIB, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})
