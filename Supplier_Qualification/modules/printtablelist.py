from Supplier_Qualification.modules.adddef import *



# --------------------------------------------------------------------------------------------------------------
# Функция вывода списка по аттестации поставщиков на странице сайта "qualification_status"

def printtablelist ():
       
    supplierlist = Supplier.objects.in_bulk()
    ttop = """
    <table class="table_st">
        <thead class="table_thead_st">
            <tr class="table_tr_st">
                <th class="table_th_td_st">#</th>
                <th class="table_th_td_st">Supplier</th>
                <th class="table_th_td_st">Commercial qualification</th>
                <th class="table_th_td_st">Product qualification</th>
            </tr>
        </thead>
    <tbody>
    """
    tcenter = ""

    tbottom ="""
    </tbody>
    </table>
    """
        
    for id in supplierlist:

        # Получение из дочерней таблицы "Product" данных по продуктовой аттестации по определённому поставщику
        products_list = Product.objects.filter(supplier__id=supplierlist[id].id)
        prod_txt = ""
       
        for product in products_list:
            prod_txt = prod_txt + product.prodName +": " + qStatusToHtml(product.prodStatus) + " " + dateToHtml(product.statusData) + "<br>"


        tcenter = (tcenter
                   + """<tr class="table_tr_st table_tr_link"><th class="table_th_td_st">"""
                   + str(supplierlist[id].id)
                   + """</th><td class="table_th_td_st bold">"""
                   + """<a class="main_link_tr" href='/qualification_status/"""
                   + str(supplierlist[id].id)
                   + """/'>"""
                   + supplierlist[id].name
                   +"""</a>"""
                   + """</td><td class="table_th_td_st">"""
                   + qStatusToHtml(supplierlist[id].cq)
                   + " "
                   + dateToHtml(supplierlist[id].cqdata)
                   + """</td><td class="table_th_td_st">"""
                   + str(prod_txt)
                   + "</td></tr>"
                   + "\n")
       
        statustable = ttop + tcenter + tbottom

    return statustable
