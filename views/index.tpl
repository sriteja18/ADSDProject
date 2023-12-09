<!DOCTYPE html>
<html>
<head>
    <title>Movies and Genre</title>
</head>
<body>
    <form action="/" method="get">
        <label>Search:</label>
        <input type="text" name="search" placeholder="Enter title or genre">
        <input type="submit" value="Search">
    </form>
    <h1>Movies and Genre</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Release Year</th>
            <th>Genre</th>
            <th>Edit</th>
            <th>Delete</th>
        </tr>
        % for movie in movies:
        <tr>
            <td>{{ movie[0] }}</td>
            <td>{{ movie[1] }}</td>
            <td>{{ movie[2] }}</td>
            <td>{{ movie[3] }}</td>
            <td><a href="/edit/{{ movie[0] }}">Edit</a></td>
            <td><a href="/delete/{{ movie[0] }}" onclick="return confirm('Are you sure you want to delete this item?');">Delete</a></td>
        </tr>
        % end
    </table>
    <p><a href="/add">Add Movie</a></p>
</body>
</html>
