def test_named_entities_extraction(client):
    
    response = client.post("/ner/extrac", data= " تم إصدار قرار بإقالة رئيس المخفر الجنوبي في مدينة جبلة ( أبو سمير ) .. ونقله إلى منطقة أخرى")
    assert response.status_code == 200
    data = response.get_json()
    print(data)
