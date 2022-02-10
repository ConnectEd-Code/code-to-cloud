from flask import Flask, request, render_template

invite_app = Flask('app')


@invite_app.route("/")
def form():
    return render_template("form.html")


@invite_app.route("/view")
def view_invite():
    # to = "Tom"
    # event = "Artemis' birthday party"
    # date = "February 10th"
    # time = "4am"
    # sender = "Jack"


    date = request.args.get('date')
    time = request.args.get('time')
    event = request.args.get('event')
    to = request.args.get('to')
    sender = request.args.get('sender')
    style = request.form.get('style')


    # http://192.168.1.122:8080/view?style=kids
    # http://192.168.1.122:8080/view?event=Bibi's+Bday&to=Clair&date=Monday+32nd+of+Mocktober&time=4pm&sender=Renee&style=cat
    style = request.args.get('style')

    template = "invite-" + style + ".html"
    

    return render_template(template, to=to, event_name=event, date=date, time=time, sender=sender)



if __name__ == '__main__':
    invite_app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)