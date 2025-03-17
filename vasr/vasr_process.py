from PIL import Image, ImageDraw, ImageFont




def create_analogy_image(image_a, image_a_prime, image_b, candidates):
    # Load images
    img_a = Image.open(image_a)
    img_a_prime = Image.open(image_a_prime)
    img_b = Image.open(image_b)
    img_b_prime_placeholder = Image.open("question_mark.png")
    candidate_images = [Image.open(candidate) for candidate in candidates]

    # Resize images to a uniform size
    img_size = (300, 300)
    img_a = img_a.resize(img_size)
    img_a_prime = img_a_prime.resize(img_size)
    img_b = img_b.resize(img_size)
    img_b_prime_placeholder = img_b_prime_placeholder.resize(img_size)
    candidate_images = [img.resize(img_size) for img in candidate_images]

    # Create a blank image for the final layout
    margin = 20
    title_height = 50
    candidate_height = 300
    spacing = 40
    width = 4 * img_size[0] + 5 * margin  # 4 images in a row
    height = img_size[1] * 2 + title_height + candidate_height + 3 * margin + spacing - 140  # Two rows + titles + candidates

    final_image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(final_image)


    font = ImageFont.load_default(25)
    title_font = ImageFont.load_default(30)

    # Add titles
    draw.text((width // 2 - 80, margin), "Analogy", fill="black", font=title_font)
    draw.text((width // 2 - 80, img_size[1] + margin + spacing + title_height), "Candidates for Y\'", fill="black", font=title_font)

    # Position and paste images
    # Row 1: A, A', B, B'
    y_offset = int(2*margin) + title_height
    x_positions = [margin, 2 * margin + img_size[0], 3 * margin + 2 * img_size[0], 4 * margin + 3 * img_size[0]]
    final_image.paste(img_a, (x_positions[0], y_offset))
    final_image.paste(img_a_prime, (x_positions[1], y_offset))
    final_image.paste(img_b, (x_positions[2], y_offset))
    final_image.paste(img_b_prime_placeholder, (x_positions[3], y_offset))

    # Add labels for A, A', B, B'
    draw.text((x_positions[0] + img_size[0] // 2 - 10, y_offset - 30), "X", fill="black", font=font)
    draw.text((x_positions[1] + img_size[0] // 2 - 10, y_offset - 30), "X'", fill="black", font=font)
    draw.text((x_positions[2] + img_size[0] // 2 - 10, y_offset - 30), "Y", fill="black", font=font)
    draw.text((x_positions[3] + img_size[0] // 2 - 10, y_offset - 30), "Y'", fill="black", font=font)

    # Row 2: Candidates
    y_offset = margin + title_height + img_size[1] + spacing + 2*margin
    for i, candidate in enumerate(candidate_images):
        x_offset = margin + i * (img_size[0] + margin)
        final_image.paste(candidate, (x_offset, y_offset))
        # Add candidate number
        draw.text((x_offset + img_size[0] // 2 - 10, y_offset + img_size[1] + 5), str(i + 1), fill="black", font=font)

    # Save the final image
    return final_image 