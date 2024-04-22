import json
import requests

from django.db.models import Q
from webhook.models import NamesMan, NamesWoman


def get_names(data: dict) -> dict:
    contacts = data.get('contacts', [])
    names = [contact.get('name') for contact in contacts]

    names_man_query = Q()
    names_woman_query = Q()

    for name in names:
        names_man_query |= Q(name=name)
        names_woman_query |= Q(name=name)

    names_man = NamesMan.objects.filter(names_man_query)
    names_woman = NamesWoman.objects.filter(names_woman_query)
    name_dict_man = {contact.name: contact for contact in names_man}
    name_dict_woman = {contact.name: contact for contact in names_woman}

    return fetch_names(data, name_dict_man, name_dict_woman)


def fetch_names(data: dict, name_dict_man: dict, name_dict_woman: dict) -> dict:
    contacts = []
    for contact in data.get('contacts', []):
        name = contact.get('name')
        contact_obj = name_dict_man.get(name) or name_dict_woman.get(name)
        if contact_obj:
            contacts.append({
                'pk': contact_obj.id,
                'id': contact.get("id"),
                'name': contact_obj.name,
                'gender': contact_obj.gender,
            })

    result = {
        "contacts": contacts,
        "back_url": data.get("back_url")
    }

    return result


def send_data_to_back_url(data: dict, url: str):
    serialized_data = json.dumps(data)
    return requests.post(url, json=serialized_data)
