import media						#Import statements for getting Movie Class and open_movies_page function.
import fresh_tomatoes

#A Movie Object.
dangal = media.Movie("Dangal", "A Story Of Women Wrestling In India",
	"https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
	"https://www.youtube.com/watch?v=x_7YlGv9u1g")

#A Movie Object.
rustom = media.Movie("Rustom", "A story about a navy man fighting for navy's pride against seniors",
	r"https://upload.wikimedia.org/wikipedia/en/9/96/Akshay_Kumar%27s-Rustom_poster.jpg",
	"https://www.youtube.com/watch?v=L83qMnbJ198")

#A Movie Object.
lunchbox = media.Movie("Lunchbox","A story about a man and his lunchbox",
	"https://upload.wikimedia.org/wikipedia/en/8/81/The_Lunchbox_poster.jpg",
	"https://www.youtube.com/watch?v=sK3R0rvnlPs")


movies = [dangal, rustom, lunchbox]         #List of moviess to be passed as argument for the function to dispaly movies.

fresh_tomatoes.open_movies_page(movies)     #Calling the function which will creat a Web page and display the movies.

