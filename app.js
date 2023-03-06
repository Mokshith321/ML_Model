const options =[];
fetch('static/Naukri_Jobs_Data.csv')
.then(response => response.text())
.then(data => {
    const parsedData = Papa.parse(data, { header: true });

    const array = document.querySelectorAll('select');

    for(i=0;i<array.length;i++){
        var name = array[i].id;
        columnValues = parsedData.data.map(row=> row[name]);
        uniqueValues = [... new Set(columnValues)]
        select= document.getElementById(array[i].id);
        const searchOption = document.createElement('option');
        searchOption.value = 'search';
        searchOption.textContent = 'Search';
        select.insertBefore(searchOption, select.firstChild);

        uniqueValues.sort();
        uniqueValues.forEach(option =>{
            const optionElement = document.createElement('option');
                optionElement.value = option;
                optionElement.textContent = option;
                select.appendChild(optionElement);
            });
                          
        idf = document.getElementById(name);
        options[i]= idf.querySelectorAll('option');                
    }
});  

