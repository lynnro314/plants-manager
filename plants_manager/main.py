from flask import Flask

app = Flask(__name__)


def main():
    app.run('0.0.0.0', port=1576)


if __name__ == '__main__':
    main()
