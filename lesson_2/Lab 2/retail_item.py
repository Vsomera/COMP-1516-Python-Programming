# COMP 1516 - Lab 2
# Vilmor Somera
# 9/20/22
import f

def main():
    item_desc = f.get_retail_item_desc()
    quan_purch = f.get_num_of_purchased_items()
    p_per_unit = f.get_price_usd_per_unit()
    tax = f.get_tax_rate()

    print("Sales Reciept:")
    print("Item Description:", item_desc)
    print("Number of Purchased items:", quan_purch)
    print("Unit Price (USD):", p_per_unit)
    print("Tax Rate:", tax)
    print("Subtotal:", f.calc_subtotal_usd(p_per_unit, quan_purch))
    subtotal_usd = f.calc_subtotal_usd(p_per_unit, quan_purch)
    print("Tax:", f.calc_tax_usd(subtotal_usd, tax))
    tax_usd =  f.calc_tax_usd(subtotal_usd, tax)
    print("Total:", f.calc_total_usd(subtotal_usd, tax_usd))
    

if __name__ == "__main__":
    main()