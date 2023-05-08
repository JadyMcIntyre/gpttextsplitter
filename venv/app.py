from flask import Flask, render_template, request
app = Flask(__name__)

def split_text(input_text, max_chars=3900):
    text_chunks = []
    start_index = 0

    while start_index < len(input_text):
        end_index = start_index + max_chars

        if end_index <= len(input_text):
            last_space = input_text.rfind(' ', start_index, end_index)
            if last_space != -1:
                end_index = last_space

        chunk = input_text[start_index:end_index].strip()
        text_chunks.append(chunk)
        start_index = end_index

    return text_chunks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        splitted_text = split_text(input_text)
        return render_template("index.html", splitted_text=splitted_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
