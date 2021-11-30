$(document).ready(function () {
$(function () {
    $('.photoUrl').click(function () {
    $(this).focus();
    $(this).select();
    document.execCommand('copy');
    alert("Link Copied to clipboard");
    });
});
});