import { createUsersApi } from "~/api/users";
import { createAuthApi } from "~/api/auth";

export const useApi = () => {
  const fetch = $fetch.create({
    baseURL: "/api",
    headers: {
      "X-CSRFToken": useCookie("csrftoken").value || ""
    },
  });

  return {
    users: createUsersApi(fetch),
    auth: createAuthApi(fetch)
  }
}
