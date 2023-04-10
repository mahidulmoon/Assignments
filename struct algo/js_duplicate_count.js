let xhr = new XMLHttpRequest();
xhr.open("GET", "{% url 'usermanagement:chartdata' %}");
xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onreadystatechange = function () {
if (xhr.readyState === 4) {
    if (xhr.status === 200){
        var jsonResponse = JSON.parse(xhr.responseText);
        // console.log("success",jsonResponse)
        var output = [];
        jsonResponse.data.forEach(function(item) {
        var existing = output.filter(function(v, i) {
            return v.month == item.month;
        });
        if (existing.length) {
            var existingIndex = output.indexOf(existing[0]);
            output[existingIndex].total = output[existingIndex].total + item.total;
        } else {
            if (typeof item.total == 'number')
            output.push(item);
        }
        });
        console.log(output)


    }else{
        var jsonResponse = JSON.parse(xhr.responseText);
        console.log("error",jsonResponse)

    }
}};

xhr.send();
