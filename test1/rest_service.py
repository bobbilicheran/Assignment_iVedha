from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    es.index(index="rbcapp1-status", body=data)
    return jsonify({"message": "Inserted into Elasticsearch"}), 201

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    res = es.search(index="rbcapp1-status", size=1000)
    services = [hit["_source"] for hit in res["hits"]["hits"]]
    overall = "UP" if all(s["service_status"] == "UP" for s in services) else "DOWN"
    return jsonify({"application_status": overall})

@app.route("/healthcheck/<service>", methods=["GET"])
def service_health(service):
    res = es.search(index="rbcapp1-status", q=f"service_name:{service}", size=1, sort="@timestamp:desc")
    if res["hits"]["hits"]:
        status = res["hits"]["hits"][0]["_source"]["service_status"]
        return jsonify({service: status})
    return jsonify({service: "UNKNOWN"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
