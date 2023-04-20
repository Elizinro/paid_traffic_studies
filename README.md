# paid_traffic_studies
Trying to learn paid traffic, using Python, facebook ADS and google ADS.

# views.py technical terms
This section is to understand the technical terms of views.

### ARC(Ajax Render Content)
Simple way to understand, you create a render (from Django render) object, containing the request, the name of the template and the context:
rendered = render(request, "template.html", context)
after that you return a JsonResponse to the ajax request:
return JsonResponse({'template_function_name': rendered.content.decode()})
and using that you change a div in the ajax to include this to the page, this is good for fast things that you able to have without refreshing the page.
ajax example:
'''$.ajax({
    type: "GET",
    url: "{% url 'the name of the url that links to the views.py' %}",
    data: {Some data if you want},
    success: function(data) {
        $("something to relate to the div, like class (.) or id (#)").html(data["name of the template_function_name that returned as JsonResponse"]);
    },
    error: function(error) {
        console.error("An error occurred:", error);
    }
});'''