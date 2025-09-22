from rembg import new_session

models_to_test = ["u2net", "u2net_human_seg", "isnet-general-use", "isnet-anime"]

for model in models_to_test:
    try:
        session = new_session(model)
        print(f"✅ Модель '{model}' - РАБОТАЕТ")
    except Exception as e:
        print(f"❌ Модель '{model}' - НЕ РАБОТАЕТ: {e}")
