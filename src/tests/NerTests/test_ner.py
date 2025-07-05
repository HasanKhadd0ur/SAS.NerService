def test_named_entities_extraction(client):
    
    response = client.post("/ner/extract", data= " تم إصدار قرار بإقالة رئيس المخفر أبوسمير الجنوبي في مدينة جبلة... ونقله إلى منطقة أخرى", content_type='text/plain')
    assert response.status_code == 200
    data = response.get_json()
    print(data)
