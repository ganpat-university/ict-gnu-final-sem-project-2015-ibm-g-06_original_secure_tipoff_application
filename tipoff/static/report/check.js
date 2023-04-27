do{
    var favDrink = prompt("You are entering a Indian government website. \n I understand that repeatedly providing tips with no investigative value will result in my tips not being considered. \n\n\n I understand that providing false information could subject me to fine, imprisonment, or both (under Indian Penal code!!). \n\n\n Please Type agree/Agree to continue!!", "I do not agree");
    switch(favDrink) {
    case "agree":
                    break;
    case "Agree":
                    break;
    default:
        window.location.href="/";
    //window.location.href="{{templates ('home/homepage.html')}}";
            break;
    }
}
while(favDrink == null || favDrink== "" );