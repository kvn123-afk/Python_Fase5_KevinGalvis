# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Solución Dinámica al Problema 5

def evaluar_jornada_laboral(horas_diarias):
    """
    Módulo para calcular la suma total de horas semanales
    y clasificar la jornada (Umbral: 40 horas).
    """
    total_horas = sum(horas_diarias)
    
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion


def main():
    print("=========================================================")
    print("   SISTEMA DE INGRESO Y AUDITORÍA DE HORAS LABORALES     ")
    print("=========================================================\n")
    
    matriz_recursos = []
    DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    for i in range(4):
        print(f"--- Registro del Recurso #{i + 1} ---")
        nombre = input("Ingrese el nombre del trabajador: ")
        
        horas_trabajador = [nombre]
        
        for dia in DIAS:
            while True:
                try:
                    horas = float(input(f"  Horas trabajadas el día {dia}: "))
                    if horas >= 0:
                        horas_trabajador.append(horas)
                        break
                    else:
                        print("  ❌ Las horas no pueden ser negativas. Intente de nuevo.")
                except ValueError:
                    print("  ❌ Entrada inválida. Por favor, ingrese un número.")
        
        matriz_recursos.append(horas_trabajador)
        print()

    print("\n=========================================================")
    print("                  INFORME DE JORNADAS                    ")
    print("=========================================================")
    print(f"{'RECURSO':<20} | {'TOTAL HORAS':<12} | {'CLASIFICACIÓN JORNADA'}")
    print("-" * 60)
    
    for recurso in matriz_recursos:
        nombre = recurso[0]
        horas_diarias = recurso[1:]
        
        total_horas, clasificacion = evaluar_jornada_laboral(horas_diarias)
        
        print(f"{nombre:<20} | {total_horas:<12.1f} | {clasificacion}")

    print("-" * 60)
    print("Proceso de auditoría finalizado con éxito.")

if __name__ == "__main__":
    main()