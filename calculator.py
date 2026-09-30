git checkout -b feature/calculator

# Коммит 1
cat > calculator.py << 'EOF'
# Calculator app
def add(a, b):
    return a + b
# TODO: add more functions
