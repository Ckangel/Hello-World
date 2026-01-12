from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!doctype html>
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #00ffff;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
      }
      h1 {
        color: #ff0000;
      }
      input {
        padding: 10px;
        margin-top: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
      }
      p {
        margin-top: 20px;
        font-size: 18px;
        color: #555;
      }
    </style>
  </head>
  <body>
    <h1>Hello World</h1>
    <label>Enter your firstname:</label>
    <input type="text" id="firstname" placeholder="Type your name here">
    <p id="greeting"></p>

    <script>
      const input = document.getElementById("firstname");
      const greeting = document.getElementById("greeting");

      input.addEventListener("input", function() {
        const name = input.value.trim();
        if (name) {
          greeting.textContent = `I'm ${name}, Hello World!!`;
          console.log(`I'm ${name}, Hello World!!`);
        } else {
          greeting.textContent = "";
        }
      });
    </script>
  </body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
