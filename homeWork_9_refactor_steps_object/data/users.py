import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    full_name: str


guest = User(first_name='Johann', last_name='Bach', user_email='Johann@Bach.com', full_name='Johann Bach')
