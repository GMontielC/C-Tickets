import json

def iterar_json(json_data):


  for key, value in json_data.items():
    print(f"{key}: {value}")


if __name__ == "__main__":
  # Creamos un JSON de ejemplo.
  json_data ={
  "event_general": 
  {
    "user_id": "ObjectId",
    "type_id": "ObjectId",
    "currency_id": "ObjectId",
    "venue_id": "ObjectId",
    "supplier_id?": "ObjectId",
    "event": [
      {
        "lang": "es",
        "title": "",
        "description": ""
      }
    ],
    "img_header?": "File",
    "img_event?": "File",
    "img_flyer?": "File",
    "url_ticket?": "https://",
    "url_streaming?": "https://",
    "sell_tickets": False,
    "sold_out": False,
    "event_info?": 
	{
      "age_limit": 4,
      "duration": "2022-12-05T17:00:48.571000",
      "info": [
        {
          "lang": "es",
          "general": "eteieojidojdp",
          "observations": "Menores de 4 años no ingresan al inmueble",
          "services": "Venta de alimentos y bebidas",
          "restrictions": "No se permiten alimenos, bebidas, camaras, etc...",
          "access_limit": "Sin limite de acceso, o 15 minutos antes de empezar."
        }
      ]
    },
    "event_costs": 
	{
      "regular": 10,
      "lower": 1200,
      "high": 3500.5
    },
    "event_schedule": 
	{
      "date": "2022-12-04T19:34:43.334000",
      "access_at": "2022-12-04T19:34:43.334000",
      "start_at": "2022-12-04T19:34:43.334000",
      "end_at": "2022-12-04T19:34:43.334000"
    },
    "event_tags": [
      {
        "lang": "es",
        "name":  "tag name"
      }
    ],
    "event_special_tags": [
      {
        "name": "Feria nacional",
        "abbreviation?": "fenaza",
        "description": 
		{
          "lang": "es",
          "description": ""
        },
        "website?": "",
        "genres?": "",
        "members?": "",
        "rewards?": "",
        "img_header?": "",
        "img_special": "",
        "color?": "",
        "active?": True,
        "dead?": False,
        "since?": "2022-12-04T19:34:43.334000",
        "birthday?": "2022-12-04T19:34:43.334000",
        "initial_date?": "2022-12-04T19:34:43.334000",
        "final_date?": "2022-12-04T19:34:43.334000",
        "tags": 
		[
          "tag_id", "tag_id"
        ],
        "address": 
		{
          "latitude": "-63572375290155",
          "longitude": "106744840359415",
          "address": "Av. Hidalgo #824",
          "address2": "Col. Centro",
          "city": "Zacatecas",
          "state": 
		  {
            "long_name": "Zacatecas",
            "short_name": "ZC"
          },
          "country": 
		  {
            "long_name": "México",
            "short_name": "MX"
          },
          "zipcode": "98000"
        }
      }
    ],
    "event_venue": 
	{
      "category_id?": "Object ID",
      "name": "Teatro Telmex",
      "quota?": 20000,
      "url?": "https://",
      "generic_rules?": "Teatro Telmex",
      "children_rules?": "Teatro Telmex",
      "accesible_seats?": True,
      "address": 
	  {
        "latitude": "-63572375290155",
        "longitude": "106744840359415",
        "address": "Av. Hidalgo #824",
        "address2": "Col. Centro",
        "city": "Zacatecas",
        "state": 
		{
          "long_name": "Zacatecas",
          "short_name": "ZC"
        },
        "country": 
		{
          "long_name": "México",
          "short_name": "MX"
        },
        "zipcode": "98000"
      },
      "boxoffice?": 
	  {
        "number": "osjos",
        "cash": True,
        "card": True,
        "debit": True
      },
      "boxoffice_schedules?": 
	  [
        {
          "day": "monday",
          "open": "08:00",
          "close": "10:00"
        },
        {
          "day": "tuestday",
          "open": "08:00",
          "close": "10:00"
        }
      ],
      "parking?": 
	  {
        "currency_id": "ObjectId",
        "location": "Front the ",
        "cost": 128
      }
    }
  }
}

  # Iteramos sobre el JSON.
  iterar_json(json_data)