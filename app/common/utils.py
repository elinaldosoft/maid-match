from typing import Union, Any

from ipware import get_client_ip

from django.http import HttpRequest


def get_ip_and_agent(request: HttpRequest) -> dict:
    try:
        agent = request.META.get('HTTP_USER_AGENT') or ''
        client_ip, _ = get_client_ip(request)
        return {'ip': client_ip, 'agent': agent[:499]}
    except AttributeError:
        return {}


def filter_dict(data: dict, extract: Union[str, list]) -> Any:
    try:
        if isinstance(extract, list):
            while extract:
                if result := filter_dict(data, extract.pop(0)):
                    return result
        shadow_data = data.copy()
        for key in extract.split('.'):
            if str(key).isnumeric():
                key = int(key)
            shadow_data = shadow_data[key]
        return shadow_data
    except (IndexError, KeyError, AttributeError):
        return None


def normalize_email(email: str) -> str:
    """
    Normalize the email address by lowercasing the domain part of it.
    """
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = email_name + '@' + domain_part
    return email.lower()
