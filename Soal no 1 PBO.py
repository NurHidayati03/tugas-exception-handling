def calculate_average(numbers):
    try:
        # Memastikan input adalah list
        if not isinstance(numbers, list):
            raise TypeError("Input harus berupa list.")
        
        # Memastikan semua elemen dalam list adalah angka
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Semua elemen dalam list harus berupa angka.")
        
        total = sum(numbers)
        average = total / len(numbers)
        return average
    
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError:
        print("List tidak boleh kosong.")

# Contoh penggunaan
result = calculate_average([5, 5, 7, 8])  # input yang benar adalah list
print(result)

# Contoh input yang salah
result = calculate_average("5, 5, 7, 8")  # input bukan list
print(result)

result = calculate_average([5, 5, '7', 8])  # input ada string
print(result)

result = calculate_average([])  # input list kosong
print(result)