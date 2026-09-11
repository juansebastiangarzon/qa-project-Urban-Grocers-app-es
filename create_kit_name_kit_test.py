import sender_stand_request
import data


# Función para cambiar el valor del parámetro name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Función para obtener un nuevo token de autenticación
def get_new_user_token():
    response = sender_stand_request.post_create_users(data.user_body)
    return response.json()["authToken"]


# Función de prueba positiva
def positive_assert(kit_body):
    auth_token = get_new_user_token()

    response = sender_stand_request.post_create_kit(
        kit_body,
        auth_token
    )

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Función de prueba negativa
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()

    response = sender_stand_request.post_create_kit(
        kit_body,
        auth_token
    )

    assert response.status_code == 400

# Prueba 1. El número permitido de caracteres (1)
def test_create_kit_1_letter_post_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# Prueba 2. El número permitido de caracteres (511)
def test_create_kit_511_letter_post_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_0_letter_post_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_post_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Prueba 5. Se permiten caracteres especiales
def test_create_kit_has_special_symbol_post_success_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

# Prueba 6. Se permiten espacios:
def test_create_kit_has_spaces_post_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# Prueba 7. Se permiten números:
def test_create_kit_has_number_post_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Prueba 8. El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_kit_no_name_post_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

# Prueba 9. Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_type_name_post_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)