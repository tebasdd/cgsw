"""
sudo apt update
sudo apt upgrade
apt install python3 pip
pip install flask

python3 swserver.py

firefox-or-any-other-browser http://localhost:8000/
firefox-or-any-other-browser http://<RasPi-IP>:8000/
"""

from flask import Flask, jsonify, redirect, render_template

from cgsw.Stopwatch import StopWatch

###########################################################################################
app = Flask(__name__)

_stopwatch = StopWatch()


@app.route('/')
def html():
    return render_template("index.html", show_buttons=False)

@app.route('/control')
def html_with_buttons():
    return render_template("index.html", show_buttons=True)


@app.route('/current')
def current():
    ret = {
        "now": _stopwatch.now(),
        "elapsed": _stopwatch.elapsed,
        "is_running": _stopwatch.is_running
    }
    return jsonify(ret)


@app.route('/run')
def run():
    _stopwatch.run()
    return redirect("/current", code=302)
    # return ""


@app.route('/stop')
def stop():
    _stopwatch.stop()
    return redirect("/current", code=302)
    # return ""


@app.route('/reset')
def reset():
    _stopwatch.reset()
    # return ""
    return redirect("/current", code=302)


if __name__ == '__main__':
    reset()
    app.run(host='0.0.0.0', port=8000)
