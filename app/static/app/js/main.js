$(function() {
    $('#province_id').on("change", function(){
        province_id = $(this).val();
        //alert("Salut");
        $.get(
            "/admin/templates/zones/getCommunes",
            {
                province_id: province_id
            },
            function(data, textStatus, jqXHR){
                $("#id_commune").html(data);
            }
        );
    });
});

///fonction js pour appeller les provinces,communes et zones dans la classe user
$(function() {
    $('#id_province').on("change", function(){
        province_id = $(this).val();
        // alert(id_province);
        $.get(
            "/admin/templates/utilisateurs/getCommunes",
            {
                province_id: province_id,
            },
            function(data, textStatus, jqXHR){
                $("#id_commune").html(data);
            }
        );
    });
});


$(function() {
    $('#id_commune').on("change", function(){
        commune_id = $(this).val();
        //alert(id_commune);
        $.get(
            "/admin/templates/utilisateurs/getZones",
            {
                commune_id: commune_id
            },
            function(data, textStatus, jqXHR){
                $("#id_zone").html(data);
            }
        );
    });
});

///fonction js pour appeller les code_centre,code_ecoles et code_participations dans la classe demandes

$(function() {
    $('#id_province').on("change", function(){
        province_id = $(this).val();
        // alert(id_commune);
        $.get(
            "/public/formulaire/getCodeCentre",
            {
                province_id: province_id
            },
            function(data, textStatus, jqXHR){
                $("#id_code_centre").html(data);
            }
        );
    });
});

$(function() {
    $('#id_code_centre').on("change", function(){
        code_centre_id = $(this).val();
        alert(id_code_centre);
        $.get(
            "/public/formulaire/getCodeEcole",
            {
                code_centre_id: code_centre_id
            },
            function(data, textStatus, jqXHR){
                $("#id_code_ecole").html(data);
            }
        );
    });
});

$(function() {
    $('#id_code_ecole').on("change", function(){
        code_ecole_id = $(this).val();
        // alert(id_commune);
        $.get(
            "/public/formulaire/getCodeParticipation",
            {
                code_ecole_id: code_ecole_id
            },
            function(data, textStatus, jqXHR){
                $("#id_code_participation").html(data);
            }
        );
    });
});


$(function() {
    $('#id_exetat').on("change", function(){
        exetat_id = $(this).val();
        // alert(id_commune);
        $.get(
            "/receptioniste/templates/demandes/getCodeParticipation",
            {
                exetat_id: exetat_id
            },
            function(data, textStatus, jqXHR){
                $("#id_code_participation").html(data);
            }
        );
    });
});