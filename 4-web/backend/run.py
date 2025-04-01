from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Iniciando o servidor...")
    app.run(debug=True, host='localhost', port=5000)

