def square_values(start, end):
    squares = []
    
    for num in range(start, end + 1):
        squares.append(num * num)

    even_squares = []
    odd_squares = []

    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print("All Squares:", squares)
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)

start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

square_values(start_range, end_range)