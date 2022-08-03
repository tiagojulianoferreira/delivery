def test_app_is_created(app):
    assert app.name == "delivery.app"


def test_config_is_loaded(config):
    """Teste sobre a config provida pelo pytest-flask"""

    assert config["DEBUG"] is False

def test_request_returns_404(client):
    """Outra fixture do pytest-flask pra implementar um cliete 
    HTTP que faz um request na aplicação, nesse caso valida se
    o servidor está de pé"""

    assert client.get("/url_que_nao_existe").status_code == 404

