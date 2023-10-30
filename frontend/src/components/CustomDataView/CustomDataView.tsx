import MenuBookIcon from "@mui/icons-material/MenuBook";
import { DataView } from "primereact/dataview";
import { useEffect, useState } from "react";
import { RecipeInterface } from "../RecipeInterfaces";
import "./CustomDataView.styles.css";

export default function CustomDataView() {
  const [recipes, setRecipes] = useState<RecipeInterface[]>([]);

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch("http://localhost:8000/recipes/all/");
        const jsonData = await response.json();
        setRecipes(jsonData);
      } catch (err: unknown) {
        console.error("Error fetching the recipe: ", err);
      }
    };
    fetchRecipes();
  }, []);

  const itemTemplate = (recipe: RecipeInterface) => {
    return (
      <div className="col-12">
        <div className="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
          <img
            className="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round"
            src={recipe.url_image}
            alt={recipe.info_recipe.title}
          />
          <div className="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
            <div className="flex flex-column align-items-center sm:align-items-start gap-3">
              <div className="text-2xl font-bold text-900">
                {recipe.info_recipe.title}
              </div>
              <div className="flex align-items-center gap-3">
                <span className="flex align-items-center gap-2">
                  <MenuBookIcon />
                  <div>
                    {Object.entries(recipe.info_recipe.nutrition).map(
                      ([key, value], index) => (
                        <span className="font-semibold" key={key}>
                          <strong>{key}:</strong> {value}
                          {index <
                            Object.entries(recipe.info_recipe.nutrition)
                              .length -
                              1 && <span className="ml-2"> </span>}
                        </span>
                      )
                    )}
                  </div>
                </span>
              </div>
              <div className="font-semibold">
                <a href={recipe.url} target="_blank">
                  {recipe.url}
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="card">
      {recipes.length > 0 && (
        <DataView
          value={recipes}
          itemTemplate={itemTemplate}
          paginator
          rows={7}
        />
      )}
    </div>
  );
}
