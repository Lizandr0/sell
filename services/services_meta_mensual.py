from repositories.repo_meta_mensual import get_meta_mensual

def obtener_meta_mensual():
    try:
        return get_meta_mensual()
    except Exception as e:
        print(f"Error al obtener la meta mensual: {e}")
        return []