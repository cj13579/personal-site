---
hide:
  - navigation
  - toc
---
# SQL Query to PostgREST URI translation

[sql2pgrest](https://github.com/cj13579/sql2pgrest) converts standard SQL that you know and love into the rather mysterious PostgREST URIs. There are bunch of decent Javascript clients out there ([SAS makes a really good one](https://github.com/sassoftware/postgrest-client)) that are much more powerful than this, but sometimes you just want to hit Swagger and try some queries. This helps with that and not much more.

## Try it out

You can try the library in the form below. Just type in an the query that you want to convert, and get a PostgREST URI back.

<style>
button {
    background-color: #04AA6D; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
</style>
<textarea wrap="off" cols="100" rows="5" id="queryInput">
SELECT first_name,last_name,dob
FROM class
WHERE age > 12
AND sex LIKE 'male'</textarea>
<small>* Your queries are not stored or collected by this site.</small>
<div class="btn-block">
    <button  name="convert2Postgrest" type="submit" onclick="convertToPostgREST()">Convert</button>
</div>
<h3 id="pgUrl"></h3>

For more information, head over to [GitHub :simple-github:](https://github.com/cj13579/sql2pgrest). 

Don't forget to give us a star :star2:.

<script>
    var textAreas = document.getElementsByTagName('textarea');
    Array.prototype.forEach.call(textAreas, function(elem) {
        elem.placeholder = elem.placeholder.replace(/\\n/g, '\n');
    });
    function convertToPostgREST() {
        var data = document.getElementById('queryInput').value;
        result = sql2postgrest(data);
        if (result) {
            if (result.success) {
                log("SUCCESS: Query converted.", "success")
                document.getElementById("pgUrl").textContent=result.message;
            } else {
                log("ERROR: Unable to convert query.", "error")
                document.getElementById("pgUrl").textContent=result.message;
            }
        } else {
            log("things have gone badly for us.")
        }
    }
</script>

