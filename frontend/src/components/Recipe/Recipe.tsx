import { Fieldset } from "primereact/fieldset";
import { useEffect, useState } from "react";
import { RecipeInterface } from "../RecipeInterfaces";
import "./Recipe.styles.css";

export default function Recipe() {
  const [recipe, setRecipe] = useState<RecipeInterface | null>(null);

  useEffect(() => {
    const fetchRecipe = async () => {
      try {
        const response = await fetch("http://localhost:8000/recipes/");
        const jsonData = await response.json();
        setRecipe(jsonData);
      } catch (err: unknown) {
        console.error("Error fetching the recipe: ", err);
      }
    };
    fetchRecipe();
  }, []);

  return (
    <div className="content-container">
      {recipe && (
        <>
          <h2>{recipe.info_recipe.title}</h2>
          <p>{recipe.info_recipe.description}</p>

          <div className="grid-content">
            <div
              className="column"
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <img alt="Recipe image" src={recipe.url_image} />
            </div>
            <div className="column">
              <Fieldset
                className="element"
                legend="Information about the recipe"
                style={{
                  backgroundColor: "transparent",
                  verticalAlign: "middle",
                }}
              >
                <div>
                  {Object.entries(recipe.info_recipe.about_recipe).map(
                    ([key, value]) => (
                      <div key={key}>
                        <strong>{key}:</strong> {value}
                      </div>
                    )
                  )}
                </div>
              </Fieldset>
            </div>
            <div className="column">
              <Fieldset
                className="element"
                legend="Nutrition facts (per serving)"
                style={{
                  backgroundColor: "transparent",
                  verticalAlign: "middle",
                }}
              >
                <div>
                  {Object.entries(recipe.info_recipe.nutrition).map(
                    ([key, value]) => (
                      <div key={key}>
                        <strong>{key}:</strong> {value}
                      </div>
                    )
                  )}
                </div>
              </Fieldset>
            </div>
          </div>

          <p>
            Certainly tempted by this delightful recipe? Eager to create it
            yourself? Unlock the secrets right{" "}
            <a href={recipe.url} target="_blank">
              here
            </a>
            !
          </p>
        </>
      )}
    </div>
  );
}
