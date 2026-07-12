from fastapi import FastAPI

app = FastAPI(title="Book Library API")


# Root endpoint — simple welcome message to confirm the server is running
@app.get("/")
def hello():
    return {"message": "Welcome to the book library"}


# Returns all books wrapped in an object (not a bare list),
# so we can add fields later (count, page, ...) without breaking clients
@app.get("/books")
def list_books():
    books = ["Data Structure", "LLMs", "Python"]
    return {"books": books, "count": len(books)}


# Path parameter: FastAPI validates that book_id is an int automatically.
# Try /books/abc in the browser and you'll get a clear 422 error — for free.
@app.get("/books/{book_id}")
def get_book(book_id: int):
    # JSON keys in snake_case — the common REST convention
    return {"book_id": book_id, "status": "available"}


# Query parameter with a default value:
# /search        -> {"searching_for": "All"}
# /search?q=llm  -> {"searching_for": "llm"}
@app.get("/search")
def search_books(q: str = "All"):
    return {"searching_for": q}