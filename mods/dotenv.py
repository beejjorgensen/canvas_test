import os

def load_dotenv():
    try:
        with open(".env") as envf:
            for line in envf:
                var, rest = line.strip().split('=', 1)
                var = var.strip()
                if var not in os.environ:
                    os.environ[var] = rest

    except FileNotFoundError:
        pass
