<script>
    $(function () {
        $("#b-more").click(function () {
            $("#cup").toggleClass("active");
            $("#basic").toggleClass("active");
        });
    });
    $(function () {
        $("#header-collapse-button").click(function () {
            $("#header-unit").toggleClass("active");
            $("#content-unit").toggleClass("active");
        });
    });
    // Ensure the DOM is fully loaded before running the script
    $(document).ready(function () {
        // Get the title of the document
        var title = $(document).attr("title");
    // Display the title inside an element with id 'titleDisplay'
    $("#titleDisplay").text(title);
    });
</script>