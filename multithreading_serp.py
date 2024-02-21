import tkinter as tk
from tkinter import scrolledtext
from googlesearch import search
import newspaper
import webbrowser

def extract_relevant_content(url, query):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()

        # Extract the relevant content based on the query
        relevant_content = article.text
        
        return relevant_content

    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

def open_link(url):
    webbrowser.open(url)

def search_and_display():
    try:
        # Get the query from the entry widget
        user_query = query_entry.get()

        result_text.delete(1.0, tk.END)  # Clear existing text

        # Use the user-entered query to get search results
        search_results = list(search(user_query, num=5, stop=5, pause=2))

        # Retrieve relevant content in parallel using multithreading
        for url in search_results:
            relevant_content = extract_relevant_content(url, user_query)

            result_text.insert(tk.END, f"\nURL: {url}\n")
            result_text.insert(tk.END, f"Relevant Content: {relevant_content}\n\n")

            # Add a hyperlink to open the link when clicked
            result_text.tag_configure(url, foreground="blue", underline=True)
            result_text.insert(tk.END, "Open Link\n", url, lambda event, u=url: open_link(u))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Query Results")

    # Entry widget for user input
    query_entry = tk.Entry(root, width=50)
    query_entry.pack(pady=10)

    # Button to trigger the search
    search_button = tk.Button(root, text="Search", command=search_and_display)
    search_button.pack(pady=5)

    # ScrolledText widget for displaying results
    result_text = scrolledtext.ScrolledText(root, width=80, height=20)
    result_text.pack(padx=10, pady=10)

    root.mainloop()

