import json
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load the updated dictionary
with open("dictionary.json", "r", encoding="utf-8") as file:
    reference_dict = json.load(file)

# Helper function to extract vendor
def extract_vendor(text):
    # Check for hashtags
    vendor_match = re.search(r"#(\S+)", text)
    if vendor_match:
        return vendor_match.group(1)
    
    # Check for known vendor names
    for vendor in reference_dict["vendors"]:
        if vendor in text:
            return vendor
    
    return "نامشخص"

# Helper function to extract commodity data
def extract_commodity_data(text):
    results = []
    lines = text.split("\n")
    date_found = None
    vendor_found = extract_vendor(text)

    # Extract the date (handles both long and short Jalali formats)
    date_match = re.search(r"مورخه\s+(\d{2,4}/\d{1,2}/\d{1,2})", text)
    if date_match:
        date_found = date_match.group(1)

    for i, line in enumerate(lines):
        # Check if any commodity type exists in the line
        for commodity_type in reference_dict["commodity_types"]:
            if commodity_type in line:
                # Extract type, grade, size, and price
                type_found = None
                grade_found = None
                size_found = None
                price_found = None

                # Find the type
                for type_ in reference_dict["types"]:
                    if type_ in line:
                        type_found = type_
                        break
                
                # Find the grade
                for grade in reference_dict["grades"]:
                    if grade in line:
                        grade_found = grade
                        break
                
                # Find the size (explicit size or standalone number)
                size_match = re.search(r"(?:سایز\s+)?([\d.]+(?:\s*الی\s*[\d.]+)?)", line)
                if size_match:
                    size_found = size_match.group(1).strip()
                else:
                    # Check for standalone sizes from the dictionary
                    for size in reference_dict["sizes"]:
                        if size in line:
                            size_found = size
                            break
                
                # Find the price (either in the same line or the next line)
                price_match = re.search(r"\b(\d{5,})0\b", line)
                if price_match:
                    price_found = price_match.group(1) + "0"
                elif i + 1 < len(lines):  # Check the next line for the price
                    next_line_price_match = re.search(r"\b(\d{5,})0\b", lines[i + 1])
                    if next_line_price_match:
                        price_found = next_line_price_match.group(1) + "0"
                
                # Add the extracted data to results
                results.append({
                    "date": date_found,
                    "vendor": vendor_found,
                    "commodity_type": commodity_type,
                    "type": type_found,
                    "grade": grade_found,
                    "size": size_found,
                    "price": price_found
                })
                break  # Process only the first matching commodity in the line
    
    return results

# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    extracted_data = extract_commodity_data(message)
    
    # Format the extracted data for response
    formatted_data = "\n".join(
        f"تاریخ: {item['date'] or 'نامشخص'}, فروشنده: {item['vendor']}, نوع: {item['commodity_type']}, نوع فولاد: {item['type'] or 'نامشخص'}, گرید: {item['grade'] or 'نامشخص'}, سایز: {item['size'] or 'نامشخص'}, قیمت: {item['price'] or 'نامشخص'}"
        for item in extracted_data
    )
    
    response = formatted_data if formatted_data else "هیچ اطلاعات مرتبطی یافت نشد."
    
    # Reply with the formatted data
    await update.message.reply_text(response)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! پیام خود را ارسال کنید تا اطلاعات مرتبط استخراج شود.")

# Main function to set up the bot
def main():
    bot_token = "7876541643:AAETxa5cAIkv6fK94hEYVfWxedE1iaH_dXg"
    application = Application.builder().token(bot_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == "__main__":
    main()
