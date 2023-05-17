
function toggle_comments(row) {
    const notSelected = row.querySelector("#comment");
    const selected = row.querySelector("#highlighted-comment");

    if (notSelected) {
        notSelected.id = "highlighted-comment"
    }
    else if (selected) {
        selected.id = "comment";
    }


}
