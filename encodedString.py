def encodedString(encoded_str):
    
    st = encoded_str.split('0')
    parts = [part for part in st if part]


    if len(parts) >= 3:
        first_name = parts[0]
        last_name = parts[1]
        id_value = parts[2] 

        result = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id_value
        }

        return result
    else:
        return None

 
encoded_str = "John000Doe000123"
parsed_data = encodedString(encoded_str)
print(parsed_data)