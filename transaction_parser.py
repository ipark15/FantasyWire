import xml.etree.ElementTree as ET

def parse_transactions(xml_text):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_text)
    ns = {'fantasy': 'http://fantasysports.yahooapis.com/fantasy/v2/base.rng'}

    transactions = []
    for txn in root.findall('.//fantasy:transaction', ns):
        txn_type = txn.find('fantasy:type', ns).text
        txn_status = txn.find('fantasy:status', ns).text
        txn_id = txn.find('fantasy:transaction_id', ns).text
        timestamp = txn.find('fantasy:timestamp', ns).text

        if txn_type == "add/drop" and txn_status == "successful":
            added = []
            dropped = []
            team_name = None

            for player in txn.findall('.//fantasy:player', ns):
                pdata = player.find('fantasy:transaction_data', ns)
                ptype = pdata.find('fantasy:type', ns).text
                pname = player.find('fantasy:name/fantasy:full', ns).text

                if ptype == "add":
                    team_name = pdata.find('fantasy:destination_team_name', ns).text
                    added.append(pname)
                elif ptype == "drop":
                    team_name = pdata.find('fantasy:source_team_name', ns).text
                    dropped.append(pname)

            transactions.append({
                "transaction_id": txn_id,
                "team_name": team_name,
                "added": added,
                "dropped": dropped,
                "timestamp": timestamp
            })

    return transactions