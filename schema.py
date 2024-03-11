# -- Create the Category table
# CREATE TABLE Category (
#     id INT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL
# );

# -- Create the Product table
# CREATE TABLE Product (
#     id INT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL
# );

# -- Create the Product_Category junction table
# CREATE TABLE Product_Category (
#     product_id INT,
#     category_id INT,
#     PRIMARY KEY (product_id, category_id),
#     FOREIGN KEY (product_id) REFERENCES Product(id),
#     FOREIGN KEY (category_id) REFERENCES Category(id)
# );


from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Define the association table for the many-to-many relationship
product_category_association = Table('product_category_association', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)

    # Define the many-to-many relationship with Category
    categories = relationship("Category", secondary=product_category_association, back_populates="products")

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    # Define the many-to-many relationship with Product
    products = relationship("Product", secondary=product_category_association, back_populates="categories")

# Create an engine to connect to your database
engine = create_engine('sqlite:///example.db')

# Create the tables
Base.metadata.create_all(engine)
