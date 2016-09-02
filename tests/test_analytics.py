from ditto.core import analytics, config


def test_analytics():
    service = analytics.MockAnalytics()
    assert service.data is not None
    assert "timestamp" in service.data
    assert "ditto_version" in service.data
    assert "user" in service.data
    assert "host" in service.data


def test_analytics_add_metrics():
    service = analytics.MockAnalytics()
    service.add_metric("a", "test")
    service.add_metric("b", 100)
    service.add_metric("c", 1.100)
    service.add_metric("d", {"test", "result"})

    data = service.get_analytics()
    assert data["a"] == "test"
    assert data["b"] == 100
    assert data["c"] == 1.100
    assert data["d"] == {"test", "result"}


def test_get_metric():
    service = analytics.MockAnalytics()
    service.add_metric("a", "test")
    result = service.get_metric("a")
    assert result == "test"


def test_deployment_metric():
    service = analytics.MockAnalytics()
    service.add_deployment_metric("sql", "/path/to/sql/file.sql", -1)
    service.add_deployment_metric("jar", "/path/to/jar/file.jar", 0)

    assert service.data["deploy"][0]["type"] == "sql"
    assert service.data["deploy"][0]["file"] == "/path/to/sql/file.sql"
    assert service.data["deploy"][0]["result"] == -1

    assert service.data["deploy"][1]["type"] == "jar"
    assert service.data["deploy"][1]["file"] == "/path/to/jar/file.jar"
    assert service.data["deploy"][1]["result"] == 0


def test_splunk_enabled():
    config.set("analytics.enabled", "Y")
    service = analytics.Splunk(url="http://0.0.0.0/api/endpoint", username="admin", password="pass")
    assert service.data is not None
    #result = service.submit()
    #assert result


def test_splunk_disabled():
    config.set("analytics.enabled", "N")
    service = analytics.Splunk(url="http://0.0.0.0/api/endpoint", username="admin", password="pass")
    assert service.data is not None
    result = service.submit()
    assert result





