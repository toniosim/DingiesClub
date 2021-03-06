#main application to run the soundboard
#run and point browser to localhost:5000

from flask import Flask, render_template, request, redirect, g
import sqlite3
import os, sys

app = Flask(__name__)
app_title = "Dingies Club"
author = "Tones"

#only one page, all on index
@app.route("/")
def main():
	#passing to index
	return render_template("index.html", author=author)

#about page
@app.route("/about")
def about():
	return render_template("about.html", app_title="About", author=author)

#hearthstone stoundboard
@app.route("/hssb")
def hssb():
	card_conn = sqlite3.connect("cards.db")
	sound_conn = sqlite3.connect("cardsounds.db")

	card_conn.row_factory = sqlite3.Row
	sound_conn.row_factory = sqlite3.Row


	card_cur = card_conn.cursor()
	sound_cur = sound_conn.cursor()

	#getting all cards and soundfiles
	card_cur.execute("SELECT * FROM cards ORDER BY cardname ASC")
	sound_cur.execute("SELECT * FROM sounds ORDER BY cardname ASC")

	card_rows = card_cur.fetchall()
	sound_rows = sound_cur.fetchall()

	card_conn.close()
	sound_conn.close()

	#passing to index
	return render_template("hssb.html", app_title="HSSB", author=author, card_rows=card_rows, sound_rows=sound_rows)

if __name__ == "__main__":
	app.run(host='0.0.0.0')