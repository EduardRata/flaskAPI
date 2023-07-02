from flask import Flask, jsonify, request

server_port = 8000

app = Flask(__name__)
app.config["DEBUG"] = True
users = [
    {
        "nume": "Ionel",
        "password": "12345asdf",
        "email": "ionel@example.com"
    },
    {
        "nume": "Dragos",
        "password": "12345asdf",
        "email": "dragos@example.com"
    }
]

@app.route("/")
def get_data():
    return users

@app.route("/users")
def get_users():
    return jsonify({"users": users})

@app.route("/users", methods=["POST"])
def add_users():
    new_user = request.get_json()
    print(new_user["email"])
    for user in users:
        if new_user["email"] == user["email"]:
            return f'{new_user["email"]} is already taken'
        else:
            users.append(new_user)
            return '', 201

@app.route("/users", methods=["DELETE"])
def delete_user():
    del_user = request.get_json()
    for user in users:
        if del_user["email"] == user["email"]:
            users.remove(user)

    return f'deleted', 410

if __name__ == '__main__':
    app.run("localhost", port=server_port, debug = True)

