<!DOCTYPE html>
<html>
<head>
    <title>Add Movie</title>
</head>
<body>
    <h1>Add Movie</h1>
    <form action="/add" method="post">
        <label>Title:</label>
        <input type="text" name="title" required><br>

        <label>Release Year:</label>
        <input type="number" name="release_year" required><br>

        <label>Genre:</label>
        <select name="genre_id">
            % for genre in genres:
            <option value="{{ genre[0] }}">{{ genre[1] }}</option>
            % end
        </select><br>

        <input type="submit" value="Add">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>
